# character_recognition_app

# 中身
```

├── backend
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── api.py
│   ├── character_predict.py
│   ├── debug.ipynb
│   ├── digits.pkl
│   ├── main.py
│   ├── models.py
│   └── train.py
├── frontend
│   ├── .gitignore
│   ├── README.md
│   ├── babel.config.js
│   ├── dist
│   │   ├── index.html
│   │   └── static
│   │      
│   ├── package.json
│   ├── public
│   │   ├── index.html
│   │   └── static
│   │       └── img
│   │           └── favicon.ico
│   ├── src
│   │   ├── App.vue
│   │   ├── assets
│   │   │   ├── logo.png
│   │   │   └── logo.svg
│   │   ├── components
│   │   │   └── draw.vue
│   │   ├── main.js
│   │   ├── plugins
│   │   │   └── vuetify.js
│   │   ├── router
│   │   │   └── index.js
│   │   ├── store
│   │   │   └── index.js
│   │   └── views
│   │       ├── About.vue
│   │       └── Home.vue
│   ├── vue.config.js
│   └── yarn.lock
├── package-lock.json
└── package.json
```

## インストール方法

```
cd charater_recognition_app
npm install
```
frontendでは
```
cd frontend
npm install
yarn build
```

backendでは、pipenvが必要なのでpipenvをインストールしてください。
```
pip install pipenv
pipenv install
```

## 起動方法
```
cd backend
pipenv run start
```
