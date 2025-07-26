//////APP//////APP//////APP//////APP//////APP//////APP//////APP/////

//////APP//////APP//////APP//////APP//////APP//////APP//////APP/////
export default function App() {
  /////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS//////
  /////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS////FUNCTIONS//////
  const { globalUser, setGlobalUser } = useUserContext();

  useEffect(() => {
    useLocalUser({
      _user: globalUser,
      _userDispatcher: setGlobalUser,
      _action: "verify",
    });
  }, []);

  //////RETURN////RETURN////RETURN////RETURN////RETURN////RETURN////RETURN
  //////RETURN////RETURN////RETURN////RETURN////RETURN////RETURN////RETURN
  return (
    <>
      <MainQueryClientProvider>
        <RouterProvider router={GlobalRouterElments} />
      </MainQueryClientProvider>
    </>
  );
}
/////TYPES////TYPES////TYPES////TYPES////TYPES////TYPES////TYPES////TYPES////
/////TYPES////TYPES////TYPES////TYPES////TYPES////TYPES////TYPES////TYPES////

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
import { useEffect } from "react";
import { useUserContext } from "./store/UserContext";
import { useLocalUser } from "./models/hooks/useLocalUser";
import { MainQueryClientProvider } from "./query/QueryProvider";
import { RouterProvider } from "react-router-dom";
import { GlobalRouterElments } from "./routes/Router";
