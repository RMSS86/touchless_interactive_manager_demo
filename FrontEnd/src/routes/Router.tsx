export const GlobalRouterElments = createBrowserRouter(
  createRoutesFromElements(
    <>
      <Route path="/" element={<RootLayout />} errorElement={<ErrorPage />}>
        <Route index={true} element={<HomePage />} />
      </Route>
    </>
  )
);
import { createRoutesFromElements, Navigate, Outlet } from "react-router";

import {
  createBrowserRouter,
  Route, //@ts-ignore
} from "react-router-dom";

import RootLayout from "../components/UI/Layout/LayOut.js";
import HomePage from "../components/pages/home/HomePage.js";
import ErrorPage from "../components/pages/error/ErrorPage.js";
