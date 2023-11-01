<template>
    <v-container fluid>
      <v-row justify="center">
        <v-col sm="6">
          <v-card class="card">
            <v-card-title class="text-center">
              <h2>Вход</h2>
            </v-card-title>
            <v-form>
              <v-text-field label="Телефонный номер"></v-text-field>
              <v-text-field
                label="Пароль"
                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                :type="showPassword ? 'text' : 'password'"
                @click:append="showPassword = !showPassword"
              ></v-text-field>
              <v-btn class="register-btn" color="primary">Войти</v-btn>
            </v-form>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        showPassword: false,
      };
    },
  };
  </script>
  
  <style scoped>
  .card {
    background-color: #333;
    color: #fff;
    height: 416px;
    width: 923px;
  }
  
  .text-center {
    text-align: center;
  }
  
  .register-btn {
    margin-top: 19.02%;
    background-color: #e2ba35;
  }
  </style>