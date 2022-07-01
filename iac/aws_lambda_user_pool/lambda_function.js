const AWS = require('aws-sdk');

const cognitoIdentityServiceProvider = new AWS.CognitoIdentityServiceProvider({ apiVersion: '2016-04-18' });

/**
 * Get details about the client
 * @param clientId ID of the app client
 * @param userPoolID ID of the user pool
 */
const getClientDetails = async (clientId, userPoolId) => {
  const params = {
    ClientId: clientId,
    UserPoolId: userPoolId,
  };

  try {
    const clientDetails = await cognitoIdentityServiceProvider
      .describeUserPoolClient(params)
      .promise();
    if (clientDetails) {
      return {
        auth: Buffer.from(`${clientDetails.UserPoolClient.ClientId}:${clientDetails.UserPoolClient.ClientSecret}`).toString('base64'),
        creationDate: clientDetails.UserPoolClient.CreationDate,
        name: clientDetails.UserPoolClient.ClientName,
      };
    }
    throw new Error(`Empty client information found for client ${clientId}`);
  } catch (err) {
    console.error(err);
  }
  return null;
};

/**
 * Get a list of the user clients as a map
 * @param userPoolId ID of the Cognito user pool
 */
const getClientsMap = async (userPoolId) => {
  const params = {
    UserPoolId: userPoolId,
    MaxResults: 60,
  };

  // TODO: keep going until theres no more clients if there are nore than 60
  // Get list of user pool app clients
  const clients = await cognitoIdentityServiceProvider.listUserPoolClients(params).promise();

  const clientsMap = clients.UserPoolClients.reduce((map, client) => {
    const newMap = { ...map };
    if (newMap[client.ClientName]) {
      console.warn(`There is already an app client with the name: ${client.ClientName}. Client will not be replaced; oldest client will be returned.`);
    } else {
      newMap[client.ClientName] = client;
    }
    return newMap;
  }, {});

  return clientsMap;
};

exports.handler = async (event, context, callback) => {
  const enhancedResponse = { ...event };

  // Get user groups
  const userGroups = event.request.groupConfiguration.groupsToOverride;
  try {
    // Get Clients mapped
    const clients = await getClientsMap(event.userPoolId);

    // Match clients to user's groups & get the client's details (ID, secret)
    const promises = [];
    userGroups.forEach((groupName) => {
      if (clients[groupName]) {
        promises.push(getClientDetails(clients[groupName].ClientId, event.userPoolId));
      }
    });
    const clientDetails = await Promise.all(promises);

    // Override the token with clients info
    enhancedResponse.response = {
      claimsOverrideDetails: {
        claimsToAddOrOverride: {
          authorizedAppClients: JSON.stringify(clientDetails),
        },
      },
    };
  } catch (err) {
    console.error(err);
  } finally {
    // Return to Amazon Cognito
    callback(null, enhancedResponse);
  }
};
