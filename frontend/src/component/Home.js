import {useEffect, useState} from "react";
import axios from "axios";

export const Home = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        const authToken = localStorage.getItem('access_token')
        console.log(authToken, "this is the auth token")
        if( authToken === null){
            window.location.href = '/login'  
        }
        else{
            (async () => {
            try {
                const {data} = await axios.get('http://localhost:8000/home/', {
                headers: {
                //   'Content-Type': 'application/json',
                  'Authorization': `Bearer ${authToken}`
                }
              });

              setMessage(data.message);
            } catch (e) {
                console.log('not authenticated')
            }
        })()};
    }, []);



    return <div className="form-signin mt-5 text-center">
        <h3>Hello {message}</h3>
        
    </div>
}