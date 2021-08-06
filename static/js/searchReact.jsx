// users can search based on a criteria --> result: providers listed for that criteria

const SearchProvider = (props) => {
    const [doctorResults, setDoctorResults] = React.useState([]);
    const [query, setQuery] = React.useState('');
    const [doctors, setDoctors] = React.useState([])

    React.useEffect(() => {
        fetch('/')
        .then((result) => result.json())
        .then((data) => {console.log(data); return data})
        .then((data) => setDoctors(data))
    }, [])

    React.useEffect(() => {
        // filter through list of doctors based on user's query input
    }, [query])

    console.log('JSX IS WORKING')

    return (
        <div> 
            <h1>Hello World!</h1>
        </div>
    );
}
 
ReactDOM.render(
    <SearchProvider />,
    document.getElementById('doctors')
);



// const doctorData = [
//     {
//         name: "Gunjan Amarnani",
//         location: "Mankhool",
//         id: 1

//     },

//     {
//         name: 'Ruchir Shah',
//         location: 'Rhode Island',
//         id:2
//     }
// ]

// function doctorDisplay(props) {
//     return (
//         <div className = "doctors">
//             <h2> Name: {props.name}</h2>
//             <h2> Location: {props.location}</h2>
//         </div>
//     );
// }

// function doctorContainer(props) {
//     const doctorDetails = [];

//     for (const doc of doctorData) {
//         doctorDetails.push(
//         <Doctor 
//          name = {doc.name}
//          location = {doc.location}
//          id = {doc.id}
//         />
//         );
//     }
//     return <React.Fragment>{doctorDetails}</React.Fragment>;
// }





  