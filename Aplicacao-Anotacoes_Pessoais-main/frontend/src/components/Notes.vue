<template>
    <div id="app">
      <header>
        <nav>
          <div class="user-actions">
            <button class="sign-out">Sign out</button>
          </div>
        </nav>

        <div class="search">

            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="search-img">
                <path fill-rule="evenodd" d="M9 3.5a5.5 5.5 0 1 0 0 11 5.5 5.5 0 0 0 0-11ZM2 9a7 7 0 1 1 12.452 4.391l3.328 3.329a.75.75 0 1 1-1.06 1.06l-3.329-3.328A7 7 0 0 1 2 9Z" clip-rule="evenodd" />
            </svg>

            <input type="text" placeholder="PERSONAL NOTES" />

            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="add">
                <path fill-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25ZM12.75 9a.75.75 0 0 0-1.5 0v2.25H9a.75.75 0 0 0 0 1.5h2.25V15a.75.75 0 0 0 1.5 0v-2.25H15a.75.75 0 0 0 0-1.5h-2.25V9Z" clip-rule="evenodd" />
            </svg>

        </div>
      </header>

      <main>
        <div>
            <carousel :per-page="1">
                <slide v-if="notes.length === 0">
                    <div class="empty-note">
                        <p>No notes available</p>
                    </div>
                </slide>
                <slide v-for="note in notes" :key="note.id">
                    <div class="note">
                        <h2>{{ note.title }}</h2>
                        <p>{{ note.content }}</p>
                        <small>Created at: {{ note.created_at }}</small>
                    </div>
                </slide>
            </carousel>
        </div>
      </main>
    </div>
  </template>
  
  <script setup>
    import { ref, onMounted } from 'vue';
    import axios from 'axios';
    import { Carousel, Slide } from 'vue-carousel';

    const userId = localStorage.getItem('user_id');
    const notes = ref([]);

    const fetchNotes = async () => {
        try {
            const response = await axios.get('http://localhost:8000/notes/load',{
                user_id: userId
            })
            notes.value = response.data;
        } catch (error) {
            console.error('Error fetching notes:', error);
        }
    };

    onMounted(fetchNotes);
  </script>
  
  <style>

    @import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');

  
    #app {
        padding: 0;
        margin: 0;
        font-family: 'Roboto';
    }
    
    header {
        background-color: #ffffff;
        font-family: 'Roboto';
        display: block;
        padding: 10px;
        width: 100vw;
        height: 20vh;
    }
    
    nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10vh;
    }

    .search {
        margin-top: 20px;
        display: flex;
        justify-content: center;
    }

    .search-img{
        height: 5vh;
        width: auto;
        color: black;
    }

    .search input {
        padding: 5px;
        font-size: 16px;
        width: 40vw;
        height: 5vh;
        border: 0px #ffffff;
        background-color: none;
        border-radius: 31px;
    }

    .search input::placeholder{
        font-weight: 600;
        font-size: larger;
        color: black;
        text-align: center;
        opacity: 1;
    }

    .add {
        height: 5vh;
        width: auto;
        color: #728AE9;
        cursor: pointer;
    }
    .add:hover{
        color: #151F8C;
    }

    .user-actions {
        position: absolute;
        right: 5vw;
        top: 2vh;
    }
    
    .user-actions .sign-out {
        background: none;
        border: none;
        color: #5f5f5f;
        cursor: pointer;
        font-size: large;
    }

    .user-actions .sign-out:hover {
        color: #151F8C;
    }
    
    main {
        display: block;
        width: 100vw;
        height: auto;
        background-color: #ffffff;
    }

  </style>