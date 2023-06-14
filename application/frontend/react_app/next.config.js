/** @type {import('next').NextConfig} */

// const path = require('path')
// require("dotenv").config({ path: path.resolve(__dirname, `/../../.env.local`) });
console.log("Looking for API_PATH")
console.log(process.env.API_PATH)

const nextConfig = {
  reactStrictMode: true,
  env: {
    // REACT_APP_API_PATH: process.env.API_PATH,
    // NEXT_PUBLIC_API_PATH: process.env.API_PATH,
    API_PATH: process.env.API_PATH,
  }
}

module.exports = nextConfig
