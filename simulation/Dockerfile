FROM node:20-alpine

WORKDIR /app/simulation/

COPY package*.json .

RUN npm install -g npm@latest

RUN npm install

COPY . .

CMD ["npm", "start"]