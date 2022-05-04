import * as React from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import { API_URL } from "../globals";

export interface ISubscriptionsProps {}

export function Subscriptions(props: ISubscriptionsProps) {
  const [subs, setSubs] = React.useState<string[]>([]);
  let [searchParams, setSearchParams] = useSearchParams();
  const navigate = useNavigate();

  function getSubs(uuid: string | null) {
    if (!uuid) {
      return;
    }
    return fetch(`${API_URL}/subscriptions/${uuid}`)
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setSubs(data);
      });
  }

  React.useEffect(() => {
    if (!searchParams.get("uuid")) {
      navigate("/");
    }
  }, [navigate, searchParams]);

  React.useEffect(() => {
    getSubs(searchParams.get("uuid"));
  }, [searchParams]);

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
          {subs.map((sub) => {
            return <div key={sub}>{sub}</div>;
          })}
        </div>
      </div>
    </div>
  );
}
