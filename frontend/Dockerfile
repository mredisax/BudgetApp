FROM node:16-alpine

WORKDIR /app

COPY package*.json ./

RUN yarn add global @vue/cli

RUN yarn install

COPY . .

CMD [ "yarn", "serve" ]

# # Użyj oficjalnego obrazu Node.js jako bazowego obrazu
# FROM node:16-alpine

# # RUN npm install -g http-server

# # Ustaw katalog roboczy na /app
# WORKDIR /app
# # Skopiuj pliki package.json i package-lock.json i zainstaluj zależności
# COPY package*.json ./app/
# RUN npm instal

# # Skopiuj resztę kodu frontendu
# COPY . .

# # Skompiluj aplikację Vue
# RUN npm run build

# EXPOSE 8080
# CMD [ "http-server", "dist" ]
# # CMD [ "npm", "run", "serve" ]
