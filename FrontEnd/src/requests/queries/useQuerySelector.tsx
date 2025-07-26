import { useQuery } from "@tanstack/react-query";
import FetchData from "../http";

export const useRunQuery = () => {
  return useQuery({
    queryKey: ["run"],
    queryFn: () => FetchData({ _endPoint: "run" }),
    gcTime: 1000 * 60 * 5,
  });
};

// async function fetchData() {
//   // Your API call or data fetching logic here
//   const response = await fetch("https://api.example.com/data");
//   const data = await response.json();
//   return data;
// }

// function MyComponent() {
//   const { data, isLoading, isError } = useQuery({
//     queryKey: ["data"], // Unique key for this query
//     queryFn: fetchData, // Pass the function itself
//   });

//   if (isLoading) {
//     return "Loading...";
//   }

//   if (isError) {
//     return "Error!";
//   }

//   return <div>{JSON.stringify(data)}</div>;
// }
