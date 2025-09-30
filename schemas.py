INPUT_SCHEMA = {
  "type": "object",
  "properties": {
    "pathParameters": {
      "type": "object",
      "properties": {
        "docType": {"type": "string"},
        "customerId": {"type": "string"}
      },
      "required": ["docType","customerId"]
    }
  }
}

OUTPUT_SCHEMA = {
  "type": "object",
  "properties": {
    "statusCode": {"type": "integer"},
    "body": {"type": "string"}
  },
  "required": ["statusCode","body"]
}
