const express = require("express");
const axios = require("axios");
const path = require("path");
const app = express();

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(express.static(path.join(__dirname, "public")));

console.log(process.env.SERVICE1_URL);
console.log(process.env.SERVICE2_URL);

// Endpoint to render the main page
app.get("/", async (req, res) => {
  try {
    // Use async/await to fetch data from services
    const godsResponse = await axios.get(process.env.SERVICE1_URL + "/gods");
    const sayingResponse = await axios.get(
      process.env.SERVICE2_URL + "/sayings"
    );

    console.log(godsResponse.data); // This will show the fetched gods data
    console.log(sayingResponse.data); // This will show the fetched sayings data

    // Render page with fetched data
    res.render("index", {
      gods: godsResponse.data,
      saying: sayingResponse.data.saying,
    });
  } catch (error) {
    console.error("Error fetching data:", error);
    res.status(500).send("Error fetching data");
  }
});

app.get("/healthy", (req, res) => {
  res.sendStatus(200).json({ status: "OK" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
