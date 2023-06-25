import axios from "axios";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

export const CreateBlog = () => {
    const [title, setTitle] = useState('')
    const [description, setDescription] = useState('')
    const [content, setContent] = useState('')
    const [authToken, setAuthToken] = useState( localStorage.getItem('access_token'))
    const navigate = useNavigate()
    const handleSubmit = async (e) => {
        console.log(authToken, "from 12)")

        e.preventDefault();

        try{
            const response = await axios.post("http://localhost:8000/api/blogs/blogs/",
            {
                'title': title,
                'description': description,
                'content': content
            },
            {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authToken}`
                }
            });
            console.log(response)

            const blogId = response.id;
            console.log(blogId)
            navigate(`blogs/${blogId}`)
            

        }catch (e) {
            console.log("Error creating blog", e)
        }

        // Clear form inputs
        setTitle('');
        setDescription('')
        setContent('');

    };

    return (
        <div>
            <h2> Create Blog</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="title"> Title:</label>
                    <input type="text" id='title' value={title} onChange={(e) => setTitle(e.target.value)} />
                </div>
                <div>
                    <label htmlFor="description"> Description:</label>
                    <input type="text" id="description" value={description} onChange={(e) => setDescription(e.target.value)} />
                </div>
                <div>
                    <label htmlFor="content"> Content:</label>
                    <textarea  id="description" value={content} onChange={(e) => setContent(e.target.value)} />
                </div>
                <button type="submit" onClick={handleSubmit}>Create Blog</button>
            </form>
        </div>
    )
}

