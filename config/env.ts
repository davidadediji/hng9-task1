import dotenv from 'dotenv';

dotenv.config();

export const port = process.env.PORT || 5000
export const bio = process.env.BIO
export const age = process.env.AGE
export const username = process.env.USERNAME


