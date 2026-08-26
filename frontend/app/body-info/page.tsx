"use client";

import { useEffect, useState } from "react";
import BodyInfoForm from "./BodyInfoForm";

export default function BodyInfoPage() {
    const [bodyInfo, setBodyInfo] = useState<any>(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const access_token = window.localStorage.getItem("access_token");
        console.log("access_token", access_token);
        const fetchBodyInfo = async () => {
            try {
                const res = await fetch("http://localhost:8000/get_body_info", {
                    cache: "no-store",
                    headers: {
                        "Content-Type": "application/json",
                        Authorization: `Bearer ${access_token}`,
                    },
                });

                if (!res.ok) {
                    return { data: null, error: new Error("Not Found") };
                }

                const data = await res.json();
                console.log("bodyInfo", data.sub);
                setBodyInfo(data);
            } catch (error) {
                console.error(error);
            } finally {
                setIsLoading(false);
            }
        };

        fetchBodyInfo();
        console.log("bodyInfo", bodyInfo);
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
            {/* 登録フォームを表示 */}
            <BodyInfoForm />
        </div>
    )
}