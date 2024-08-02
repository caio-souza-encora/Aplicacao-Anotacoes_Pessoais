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

            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="add" @click.prevent="create_note">
                <path fill-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25ZM12.75 9a.75.75 0 0 0-1.5 0v2.25H9a.75.75 0 0 0 0 1.5h2.25V15a.75.75 0 0 0 1.5 0v-2.25H15a.75.75 0 0 0 0-1.5h-2.25V9Z" clip-rule="evenodd" />
            </svg>

        </div>
      </header>

      <main>
        <div class="container">
            <Carousel :per-page="1">
                <Slide v-if="notes.length === 0">

                    <div class="empty-note">
                        <p>No notes available</p>
                    </div>

                </Slide>
                <Slide v-for="note in notes" :key="note.id">

                    <div class="note">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="edit" @click.prevent="edit_note">
                            <path stroke-linecap="round" stroke-linejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125" />
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="delete" @click.prevent="delete_note">
                            <path stroke-linecap="round" stroke-linejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
                        </svg>
                        <h2>{{ note.title }}</h2>
                        <p>{{ note.content }}</p>
                    </div>
                    <small>Created at: {{ note.created_at }}</small>

                </Slide>
            </Carousel>
        </div>

        <div class="edit_create-note">
            <form>
                <input type="text" class="note-title" v-model="title" placeholder="Title" />
                <input type="text" class="note-content" v-model="content" placeholder="Content" />
                <button class="edit_save-button" @click.prevent="edit">Save</button>
                <button class="create_save-button" @click.prevent="create">Save</button> 
            </form>
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
    const title = ref();
    const content = ref();


    const fetchNotes = async () => {
        try {
            const response = await axios.get('http://localhost:8000/notes/load/',{
                user_id: userId
            })
            notes.value = response.data;
        } catch (error) {
            console.error('Error fetching notes:', error);
        }
    };

    onMounted(fetchNotes);

    const create_note = {

    }

    const edit_note = {
        
    }


    const create = async () => {
        try{
            const response = await axios.post('http://localhost:8000/notes/create',{
                notes_input: {
                    user_id: userId,
                    title: title,
                    content: content
                }
            })
        }
        catch (error){
            console.error('Error while creating:', error);
        }
    }

    const edit = async () => {
        try{
            const response = await axios.post('http://localhost:8000/notes/edit',{
                notes_input: {
                    id: notes.id,
                    user_id: userId,
                    title: title,
                    content: content,
                    created_at: notes.created_at,
                    updated_at: notes.updated_at
                }
            })
        }
        catch (error){
            console.error('Error while editing:', error);
        }
    }

    const delete_note = async () => {
        try{
            const response = await axios.post('http://localhost:8000/notes/delete',{
                note: notes
            })
        }
        catch (error){
            console.error('Error while deleting:', error);
        }
    }
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

    .edit_create-notes {
        display: none;
    }

    .note {
        background-color: #151F8C;
        color: white;
        height: 200px;
        width: 200px;
    }

    .container {
        display: flex;
        flex-wrap: wrap;
    }
  </style>