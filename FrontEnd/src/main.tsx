import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { UserContextProvider } from "./store/UserContext.tsx";
import App from "./App.tsx"; // @ts-ignore
import "./sass/base/_page.scss";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <UserContextProvider>
      <App />
    </UserContextProvider>
  </StrictMode>
);
