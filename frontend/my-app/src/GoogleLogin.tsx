import { GoogleLogin } from "react-google-login";
import React from "react";

const fail = (response: any) => {
  console.log("failed to login");
  console.log(response);
};

const success = (response: any) => {
  console.log("login success");
  console.log(response);
};

type Props = {};

export default function GoogleLoginCompenent({}: Props) {
  return (
    <GoogleLogin
      clientId="480144012793-h93d7ntm7bb0qm4tpmqq1tp0ip2depcf.apps.googleusercontent.com"
      buttonText="Login"
      onSuccess={success}
      onFailure={fail}
      redirectUri={"http://localhost:3000/success"}
      isSignedIn={true}
    />
  );
}
