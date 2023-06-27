import { useParams } from 'react-router-dom';
import axios from "axios";
import { useEffect, useState } from 'react';

export const BlogDetail = () => {
  const { id } = useParams(); // Access the blog ID from the route parameters
  const [blog, setBlog] = useState({})
  // Assuming you have a blogs array with the data

  useEffect(() => {
    const fetchBlogDetail = async() => {
      try {
          const response = await axios.get(`http://localhost:8000/api/blogs/blogs/${id}/`);
          console.log(response.data, "from 13")
          setBlog(response.data);
      } catch (error) {
          console.error(error)
      }
  }; 
    fetchBlogDetail();  
  }, [id])
  

  if (!blog) {
    return <div>Blog not found</div>;
  }

  return (
    <div>
      <h1>{blog.title}</h1>
      <p>{blog.description}</p>
      <p>{blog.content}</p>
    </div>
  );
}

