import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Home } from "./routes/Home";
import { LoginSuccess } from "./routes/LoginSuccess";
import { Subscriptions } from "./routes/Subscriptions";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/">
          <Route index element={<Home />} />
        </Route>
        <Route path="/success">
          <Route index element={<LoginSuccess />} />
        </Route>
        <Route path="/subscriptions">
          <Route index element={<Subscriptions />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
