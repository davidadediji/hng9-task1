"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const env_1 = require("./config/env");
const app = (0, express_1.default)();
app.get('/', (req, res) => {
    res.json({
        "slackUsername": env_1.username,
        "backend": true,
        "age": env_1.age,
        "bio": env_1.bio
    });
});
app.listen(env_1.port, () => {
    console.log(`listening on port ${env_1.port}`);
});
