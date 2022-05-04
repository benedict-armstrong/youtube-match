import * as React from "react";
import { Link, useNavigate, useSearchParams } from "react-router-dom";
import { API_URL } from "../globals";

export interface ILoginSuccessProps {}

export function LoginSuccess(props: ILoginSuccessProps) {
  let [searchParams, setSearchParams] = useSearchParams();
  let [copied, setCopied] = React.useState(false);
  const navigate = useNavigate();

  const clipBoard = (className?: string, clipped: boolean = false) => {
    return !clipped ? (
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="12"
        height="12"
        fill="currentColor"
        className={className}
        viewBox="0 0 16 16"
      >
        <path d="M3.5 2a.5.5 0 0 0-.5.5v12a.5.5 0 0 0 .5.5h9a.5.5 0 0 0 .5-.5v-12a.5.5 0 0 0-.5-.5H12a.5.5 0 0 1 0-1h.5A1.5 1.5 0 0 1 14 2.5v12a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 14.5v-12A1.5 1.5 0 0 1 3.5 1H4a.5.5 0 0 1 0 1h-.5Z" />
        <path d="M10 .5a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5.5.5 0 0 1-.5.5.5.5 0 0 0-.5.5V2a.5.5 0 0 0 .5.5h5A.5.5 0 0 0 11 2v-.5a.5.5 0 0 0-.5-.5.5.5 0 0 1-.5-.5Z" />
      </svg>
    ) : (
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="12"
        height="12"
        fill="currentColor"
        className={className}
        viewBox="0 0 16 16"
      >
        <path d="M9.5 0a.5.5 0 0 1 .5.5.5.5 0 0 0 .5.5.5.5 0 0 1 .5.5V2a.5.5 0 0 1-.5.5h-5A.5.5 0 0 1 5 2v-.5a.5.5 0 0 1 .5-.5.5.5 0 0 0 .5-.5.5.5 0 0 1 .5-.5h3Z" />
        <path d="M3 2.5a.5.5 0 0 1 .5-.5H4a.5.5 0 0 0 0-1h-.5A1.5 1.5 0 0 0 2 2.5v12A1.5 1.5 0 0 0 3.5 16h9a1.5 1.5 0 0 0 1.5-1.5v-12A1.5 1.5 0 0 0 12.5 1H12a.5.5 0 0 0 0 1h.5a.5.5 0 0 1 .5.5v12a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5v-12Z" />
        <path d="M10.854 7.854a.5.5 0 0 0-.708-.708L7.5 9.793 6.354 8.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0l3-3Z" />
      </svg>
    );
  };

  React.useEffect(() => {
    if (!searchParams.get("uuid")) {
      navigate("/");
    }
  }, [navigate, searchParams]);

  React.useEffect(() => {
    setTimeout(() => {
      setCopied(false);
    }, 3000);
  }, [copied]);

  return (
    <>
      <div className="w-screen h-screen flex justify-center items-center">
        <div>
          <div className="text-center">
            <h1 className="text-lg font-semibold text-gray-800">
              Login Successful!
            </h1>
            <p>
              Send the link below to your friends to find out which channels you
              have in common :).
              <br /> If both of you have logged in go here:{" "}
              <Link
                className="underline text-blue-400"
                to={`/subscriptions/${searchParams.get("uuid")}`}
              >
                Subscriptions in common
              </Link>
            </p>
          </div>
          <div className="flex justify-center items-center">
            <code className="block whitespace-pre overflow-x-scroll bg-gray-200 border-gray-500 px-4 py-1 rounded-md m-2">
              {"youtube.benarmstro.ng?uuid=" + searchParams.get("uuid")}
            </code>
            <button
              title="Copy link"
              type="button"
              onClick={() => {
                const text =
                  "youtube.benarmstro.ng?uuid=" + searchParams.get("uuid");
                navigator.clipboard.writeText(text).then(
                  function () {
                    setCopied(true);
                    console.log("Async: Copying to clipboard was successful!");
                  },
                  function (err) {
                    alert("Couldn't copy to clipboard, just do it manually :)");
                  }
                );
              }}
            >
              {clipBoard("h-5 w-5", copied)}
            </button>
          </div>
          <div className="flex justify-center items-center m-5">
            <p hidden={!copied} className="underline text-lg">
              Copied!
            </p>
          </div>
        </div>
      </div>
    </>
  );
}
