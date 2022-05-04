import * as React from "react";
import { useSearchParams } from "react-router-dom";
import { GoogleButtonComponent } from "../components/GoogleButton";
import { API_URL } from "../globals";

export interface IHomeProps {}

const handleClick = (uuid: string | null) => {
  const url = uuid
    ? `${API_URL}/login/url?uuid=${uuid}`
    : `${API_URL}/login/url`;
  fetch(url)
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      window.location.href = data.url;
    });
  //alert("Click");
};

export function Home(props: IHomeProps) {
  let [searchParams, setSearchParams] = useSearchParams();

  return (
    <div className="w-screen h-screen flex justify-center items-center">
      <div>
        <div className="text-center">
          <h1 className="text-lg font-semibold text-gray-800">Youtube Match</h1>
          <p>
            Click the sign in button to start. You will be asked to sign in
            using Google and the get a link to share with your friends.
          </p>
        </div>
        <div className="flex justify-center items-center">
          <button className="p-2 rounded-md boder-2 border-gray-200 m-2">
            <GoogleButtonComponent
              onClick={handleClick}
              uuid={searchParams.get("uuid")}
            ></GoogleButtonComponent>
          </button>
        </div>
      </div>
    </div>
  );
}
