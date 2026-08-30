"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import BodyInfoForm from "./BodyInfoForm";

export default function BodyInfoPage() {
    const [bodyInfo, setBodyInfo] = useState<any>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [message, setMessage] = useState("");
    const router = useRouter();

    const fetchBodyInfo = async () => {
        const access_token = window.localStorage.getItem("access_token");

        try {
            const res = await fetch(
                "http://localhost:8000/get_body_info", 
                {
                    cache: "no-store",
                    headers: {
                        "Content-Type": "application/json",
                        Authorization: `Bearer ${access_token}`,
                    },
                }
            );

            if (res.status === 401) {
                localStorage.removeItem("access_token");
                router.push("/login");
                return;
            }

            if (res.status === 404) {
                setMessage("身体情報が見つかりませんでした。登録してください。");
                return;
            }

            if (!res.ok) {
                return;
            }

            const data = await res.json();
            setBodyInfo(data);
            setMessage("");

        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => {  
        fetchBodyInfo();
    }, []);

if (isLoading) {
    return <div className="container-app">読み込み中...</div>;
}
    return (
        <div className="container-app">
            <h1 className="text-2xl font-bold mb-6">身体情報</h1>

            <div className="card">
                <div className="kpi">
                    <div className="kpi-label">身長</div>
                    <div className="kpi-value">{bodyInfo?.height ?? "-"} cm</div>
                </div>
            </div>

            <div className="card mt-3">
                <div className="kpi">
                    <div className="kpi-label">体重</div>
                    <div className="kpi-value">{bodyInfo?.weight ?? "-"} kg</div>
                </div>
            </div>

            <div className="card mt-3">
                <div className="kpi">
                    <div className="kpi-label">生活レベル</div>
                    <div className="kpi-value">{bodyInfo?.activity_status ?? "-"}</div>
                </div>
            </div>
            {message && (
                <p className="mt-4 text-green-500 font-bold">{message}</p>
            )}
            <BodyInfoForm onSuccess={fetchBodyInfo} />
        </div>
    )
}