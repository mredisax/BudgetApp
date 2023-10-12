# Użyj oficjalnego obrazu Node.js jako bazowego obrazu
FROM node:14

# Ustaw katalog roboczy na /app
WORKDIR /app

# Skopiuj pliki package.json i package-lock.json i zainstaluj zależności
COPY frontend/package*.json ./
RUN npm install

# Skopiuj resztę kodu frontendu
COPY frontend .

# Skompiluj aplikację Vue
RUN npm run build


EXPOSE 8080
CMD [ "npm", "run", "serve" ]
