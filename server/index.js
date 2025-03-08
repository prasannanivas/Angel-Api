const express = require("express");
const parser = require("./build/Release/parser.node");

const app = express();
app.use(express.json());

app.post("/parse-int64", (req, res) => {
  if (!req.body || !req.body.data) {
    return res.status(400).json({ error: "Missing binary data" });
  }

  // Convert input array to Uint8Array
  const buffer = new Uint8Array(req.body.data);
  const parsedValue = parser.getInt64FromBytes(buffer);

  res.json({ parsedInt64: parsedValue });
});

const PORT = 5000;
app.listen(PORT, () =>
  console.log(`🚀 Server running on http://localhost:${PORT}`)
);
