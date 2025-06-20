import React, { useEffect, useRef } from "react";
import { connectJobLogStream } from "../../services/websocket";

interface Props {
  userId: string;
  jobId: number;
}

const JobLogStream: React.FC<Props> = ({ userId, jobId }) => {
  const logRef = useRef<HTMLPreElement>(null);

  useEffect(() => {
    const ws = connectJobLogStream(userId, jobId, (msg) => {
      if (logRef.current) logRef.current.textContent += msg;
    });
    return () => ws.close();
  }, [userId, jobId]);

  return <pre ref={logRef} style={{background:"#222",color:"#eee",padding:12,minHeight:100}} />;
};

export default JobLogStream;