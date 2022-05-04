import * as React from "react";
import { useNavigate, useParams, useSearchParams } from "react-router-dom";
import { API_URL } from "../globals";

export interface ISubscriptionsProps {}

export function Subscriptions(props: ISubscriptionsProps) {
  const [subs, setSubs] = React.useState<string[]>([]);
  let { uuid } = useParams();
  const navigate = useNavigate();

  function getSubs(uuid: string | undefined) {
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
    if (!uuid) {
      navigate("/");
    }
  }, [navigate, uuid]);

  React.useEffect(() => {
    getSubs(uuid);
  }, [uuid]);

  return (
    <div className="w-screen h-screen flex justify-center items-center">
      <div>
        <div className="text-center">
          <h1 className="text-lg font-semibold text-gray-800">Youtube Match</h1>
          <p>Channels you both subscribe to:</p>
        </div>
        <div className="flex justify-center items-center">
          {subs.map((sub) => {
            return (
              <div className="m-2" key={sub}>
                {sub}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
