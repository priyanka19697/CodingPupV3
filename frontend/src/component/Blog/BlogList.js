import {useEffect, useState} from "react";
import axios from "axios";
import { Button } from "bootstrap";
import { useNavigate } from "react-router-dom";


export const BlogList = () => {
    const [blogs, setBlogs ]= useState([]);
    const navigate = useNavigate()
    useEffect(() => {
        const fetchBlogs = async() => {
            try {
                const response = await axios.get('http://localhost:8000/api/blogs/blogs/');
                setBlogs(response.data);
            } catch (error) {
                console.error(error)
            }
        };
        fetchBlogs();  
    }, []);

    const handleClick = () => {
      navigate('/blogs/create');
    }

    return (
      <div>
      <h2>Blogs</h2>
      {blogs.length > 0 ? (
        <ul>
          {blogs.map(blog => (
            <li key={blog.id}> <a href={`/blogs/${blog.id}`}>{blog.title}</a></li>
          ))}
        </ul>
      ) : (
        <p>Nothing yet</p>
      )}
      <button onClick={handleClick}>Create Blog</button>
    </div>
  );
};