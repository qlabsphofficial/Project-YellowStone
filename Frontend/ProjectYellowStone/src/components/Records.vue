<template>
    <div id="table-container">
        <h1>Logs</h1>

        <div id="logs-container">
            <table>
                <th>Date and Time</th>
                <th>Analysis</th>
                <th></th>

                <tr v-for="record in records" :key="record">
                    <td>{{ record.date_recorded }}</td>
                    <td>{{ record.analysis }}</td>
                    <td><button @click="delete_data(record.id)">Delete</button></td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
import current_address from '@/address';

export default {
    name: 'Records',
    methods: {
        async retrieve_data(){
            const response = await fetch(`${current_address}/retrieve_records`);
            const data = await response.json();
            
            if (response.ok){
                this.records = data.payload;
            }
            else {
                console.log('Request failed.');
            }
        },

        async delete_data(entry_id){
            const response = await fetch(`${current_address}/delete_entry?entry_id=${entry_id}`);
            const data = response.json();

            if (!response.ok){
                console.log('Failed.');
            }
            else {
                console.log(data.response);
                this.retrieve_data();
            }
        }
    },

    data() {
        return {
            records: [],
            intervalId: null
        }
    },

    mounted(){
        this.retrieve_data();
        
        this.intervalId = setInterval(() => {
            this.retrieve_data();
        }, 10000)
    },
    beforeUnmount(){
        if (this.intervalId) {
            clearInterval(this.intervalId);
        }
    }
}
</script>

<style scoped lang="scss">
#table-container {
    height: 80%;
    width: 90%;
    display: flex;
    flex-direction: column;
    transform: translateY(-5%);
    opacity: 0;
    animation: hoverIn .6s ease-in-out;
    animation-fill-mode: forwards;
}

#logs-container {
    height: 100%;
    width: 100%;
    border-radius: 15px;
    box-shadow: 2px 2px 5px #C9C9C9;
    overflow: auto; /* Add overflow: auto to enable scrolling if the content is larger than the container */

    table {
        width: 100%;
        border-collapse: collapse; /* Combine borders for adjacent cells */
    }

    th, td {
        padding: 10px;
        text-align: center;
        border: 1px solid #ccc;
    }

    th {
        background-color: rgb(0, 53, 102);
        color: white;
        border-collapse: collapse;
        border: none;
        position: sticky;
        top: 0;
    }
}

@keyframes hoverIn {
    0% {
        opacity: 0;
    }

    100% {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>