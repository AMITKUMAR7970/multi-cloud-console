import React, { useEffect, useState } from "react";
import { fetchNotifications } from "../../services/api";

const NotificationList: React.FC = () => {
  const [notifs, setNotifs] = useState<any[]>([]);

  useEffect(() => {
    fetchNotifications().then(setNotifs);
  }, []);

  return (
    <div>
      <h4>Notifications</h4>
      <ul>
        {notifs.map(n => (
          <li key={n.id}>
            [{n.type}] {n.message} {n.read ? "" : <b>(unread)</b>}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NotificationList;