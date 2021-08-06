import React, { useState, useEffect } from 'react'

export default function App() {
    const [resourceType, setResourceType] = useState('Home')

    useEffect (() => {
        console.log('test')
        },[resourceType] ) 

return (
    <>
    <div>
        <button onClick={() => setResourceType('Home')}>Home</button>
        <button onClick={() => setResourceType('Doctors')}>Doctors</button>
        <button onClick={() => setResourceType('Facilities')}>Facilities</button>
    </div>
    <h1>{resourceType}</h1>
    </>
)
}
