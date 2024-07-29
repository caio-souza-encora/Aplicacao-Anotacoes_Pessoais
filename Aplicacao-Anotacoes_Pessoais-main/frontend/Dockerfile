# Use uma imagem base com Node.js
FROM node:18

# Defina o diretório de trabalho
WORKDIR /app

# Copie o package.json e o package-lock.json
COPY package*.json ./

# Instale as dependências
RUN npm install

# Copie o restante do código da aplicação
COPY . .

# Compile a aplicação
RUN npm run build

# Exponha a porta 8080
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["npm", "run", "dev"]