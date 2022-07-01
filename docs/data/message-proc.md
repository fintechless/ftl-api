# Processed Message

## Characteristics

- [x] Category: Runtime
- [x] Requirements: regional, mutable, cachable, low latency
- [x] Source: kafka
- [x] Identifier: ftl-msg-{in/out}-{message_type}

## Definition

Different for each message type. See [message.md](../message.md) for more details.

## Examples

```json
{
  "message_type": "pacs.008",
  "content_type": "text/xml",
  "storage_path": "in/2022/02/07/17/56/08/200-0500/2feba8ae-2aa9-47d4-966b-0b8484f198e6-pacs.008.001.10.xml",
  "message_raw": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Document xmlns=\"urn:iso:std:iso:20022:tech:xsd:pacs.008.001.10\"><FIToFICstmrCdtTrf><GrpHdr><MsgId>BBBB/150928-CCT/JPY/123</MsgId><CreDtTm>2015-09-28T16:00:00</CreDtTm><NbOfTxs>1</NbOfTxs><SttlmInf><SttlmMtd>COVE</SttlmMtd><InstgRmbrsmntAgt><FinInstnId><BICFI>CCCCJPJT</BICFI></FinInstnId></InstgRmbrsmntAgt><InstdRmbrsmntAgt><FinInstnId><BICFI>AAAAJPJT</BICFI></FinInstnId></InstdRmbrsmntAgt></SttlmInf><InstgAgt><FinInstnId><BICFI>BBBBUS33</BICFI></FinInstnId></InstgAgt><InstdAgt><FinInstnId><BICFI>AAAAGB2L</BICFI></FinInstnId></InstdAgt></GrpHdr><CdtTrfTxInf><PmtId><InstrId>BBBB/150928-CCT/JPY/123/1</InstrId><EndToEndId>ABC/4562/2015-09-08</EndToEndId><TxId>BBBB/150928-CCT/JPY/123/1</TxId></PmtId><PmtTpInf><InstrPrty>NORM</InstrPrty></PmtTpInf><IntrBkSttlmAmt Ccy=\"JPY\">10000000</IntrBkSttlmAmt><IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt><ChrgBr>SHAR</ChrgBr><Dbtr><Nm>ABC Corporation</Nm><PstlAdr><StrtNm>Times Square</StrtNm><BldgNb>7</BldgNb><PstCd>NY 10036</PstCd><TwnNm>New York</TwnNm><Ctry>US</Ctry></PstlAdr></Dbtr><DbtrAcct><Id><Othr><Id>00125574999</Id></Othr></Id></DbtrAcct><DbtrAgt><FinInstnId><BICFI>BBBBUS33</BICFI></FinInstnId></DbtrAgt><CdtrAgt><FinInstnId><BICFI>AAAAGB2L</BICFI></FinInstnId></CdtrAgt><Cdtr><Nm>DEF Electronics</Nm><PstlAdr><StrtNm>Mark Lane</StrtNm><BldgNb>55</BldgNb><PstCd>EC3R7NE</PstCd><TwnNm>London</TwnNm><Ctry>GB</Ctry><AdrLine>Corn Exchange 5th Floor</AdrLine></PstlAdr></Cdtr><CdtrAcct><Id><Othr><Id>23683707994215</Id></Othr></Id></CdtrAcct><Purp><Cd>GDDS</Cd></Purp><RmtInf><Strd><RfrdDocInf><Tp><CdOrPrtry><Cd>CINV</Cd></CdOrPrtry></Tp><Nb>4562</Nb><RltdDt>2015-09-08</RltdDt></RfrdDocInf></Strd></RmtInf></CdtTrfTxInf></FIToFICstmrCdtTrf></Document>",
  "message_proc": {
    "Document": {
      "@xmlns": "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.10",
      "FIToFICstmrCdtTrf": {
        "GrpHdr": {
          "MsgId": "BBBB/150928-CCT/JPY/123",
          "CreDtTm": "2015-09-28T16:00:00",
          "NbOfTxs": "1",
          "SttlmInf": {
            "SttlmMtd": "COVE",
            "InstgRmbrsmntAgt": {
              "FinInstnId": {
                "BICFI": "CCCCJPJT"
              }
            },
            "InstdRmbrsmntAgt": {
              "FinInstnId": {
                "BICFI": "AAAAJPJT"
              }
            }
          },
          "InstgAgt": {
            "FinInstnId": {
              "BICFI": "BBBBUS33"
            }
          },
          "InstdAgt": {
            "FinInstnId": {
              "BICFI": "AAAAGB2L"
            }
          }
        },
        "CdtTrfTxInf": {
          "PmtId": {
            "InstrId": "BBBB/150928-CCT/JPY/123/1",
            "EndToEndId": "ABC/4562/2015-09-08",
            "TxId": "BBBB/150928-CCT/JPY/123/1"
          },
          "PmtTpInf": {
            "InstrPrty": "NORM"
          },
          "IntrBkSttlmAmt": {
            "@Ccy": "JPY",
            "#text": "10000000"
          },
          "IntrBkSttlmDt": "2015-09-29",
          "ChrgBr": "SHAR",
          "Dbtr": {
            "Nm": "ABC Corporation",
            "PstlAdr": {
              "StrtNm": "Times Square",
              "BldgNb": "7",
              "PstCd": "NY 10036",
              "TwnNm": "New York",
              "Ctry": "US"
            }
          },
          "DbtrAcct": {
            "Id": {
              "Othr": {
                "Id": "00125574999"
              }
            }
          },
          "DbtrAgt": {
            "FinInstnId": {
              "BICFI": "BBBBUS33"
            }
          },
          "CdtrAgt": {
            "FinInstnId": {
              "BICFI": "AAAAGB2L"
            }
          },
          "Cdtr": {
            "Nm": "DEF Electronics",
            "PstlAdr": {
              "StrtNm": "Mark Lane",
              "BldgNb": "55",
              "PstCd": "EC3R7NE",
              "TwnNm": "London",
              "Ctry": "GB",
              "AdrLine": "Corn Exchange 5th Floor"
            }
          },
          "CdtrAcct": {
            "Id": {
              "Othr": {
                "Id": "23683707994215"
              }
            }
          },
          "Purp": {
            "Cd": "GDDS"
          },
          "RmtInf": {
            "Strd": {
              "RfrdDocInf": {
                "Tp": {
                  "CdOrPrtry": {
                    "Cd": "CINV"
                  }
                },
                "Nb": "4562",
                "RltdDt": "2015-09-08"
              }
            }
          }
        }
      }
    }
  }
}
```
