"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function Dashboard() {
    const [bodyInfo, setBodyInfo] = useState<any>(null);
    const [isBodyInfoIsLoading, setBodyInfoIsLoading] = useState(true);
    const [BodyInfoMessage, setBodyInfoMessage] = useState("");
    const [intakes, setIntakes] = useState<any[]>([]);
    const [isIntakesInfoIsLoading, setIntakesInfoIsLoading] = useState(false);
    const [IntakesInfoMessage, setIntakesInfoMessage] = useState<string | null>(null);
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
                setBodyInfoMessage("身体情報が見つかりませんでした。登録してください。");
                return;
            }

            if (!res.ok) {
                return;
            }

            const data = await res.json();
            setBodyInfo(data);
            setBodyInfoMessage("");

        } finally {
            setBodyInfoIsLoading(false);
        }
    };
    const fetchIntakes = async () => {
        const access_token = localStorage.getItem("access_token");
        try {
            const res = await fetch(
                `http://localhost:8000/get_intakes_info`,
                { 
                    cache: "no-store",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${access_token}`
                    },
                }
            );
            if (res.status === 401) {
                localStorage.removeItem("access_token");
                router.push("/login");
                return;
            }

            if (!res.ok) {
                throw new Error(`API Error: ${res.status}`);
            }
            const intakes = await res.json();
            console.log("intakes", intakes);
            if (Array.isArray(intakes) && intakes.length === 0) {
                setIntakes([]);
                setIntakesInfoMessage("食事情報が見つかりませんでした。登録してください。");
            }
            setIntakes(intakes);
        } finally {
            setIntakesInfoIsLoading(false);
        }
    };

    useEffect(() => {  
        fetchBodyInfo();
        fetchIntakes();
    }, []);

if (isBodyInfoIsLoading) {
    return <div className="container-app">読み込み中...</div>;
}
if (isIntakesInfoIsLoading) {
    return <div className="container-app">読み込み中...</div>;
}
    let all_calory = 0;
    let all_protein = 0;

    intakes.forEach((intake: any) => {
        all_calory += parseInt(intake.calory);
        all_protein += parseInt(intake.protein);
    });
    return (
        <div className="container-app">
            {/* 体重 */}
            <h1 className="text-2xl font-bold mb-6">今日の状態</h1>
            <div className="card mt-3">
                <div className="kpi">
                    <p className="kpi-label">体重</p>
                    <div className="kpi-value">{bodyInfo?.weight ?? "-"} kg</div>
                </div>
            
                {BodyInfoMessage && (
                    <p className="mt-4 text-green-500 font-bold">{BodyInfoMessage}</p>
                )}
                <p className="kpi-label">カロリー</p>
                <p className="kpi-value"> {all_calory} kcal</p>
                <p className="kpi-label">タンパク質</p>
                <p className="kpi-value"> {all_protein} g</p>
            </div>
            {/* ボタン押下でbody-info画面に遷移する */}
            <div className="flex gap-4">
                <button
                    className="
                    flex-1
                    bg-green-500
                    hover:bg-green-600
                    active:bg-green-700
                    text-white
                    font-semibold
                    rounded-xl
                    px-6
                    py-4
                    transition-colors
                    duration-150
                    mt-4"
                    onClick={() => router.push("/body-info")}
                >
                    身体情報
                </button>
        
                <button
                    className="
                    flex-1
                    bg-green-500
                    hover:bg-green-600
                    active:bg-green-700
                    text-white
                    font-semibold
                    rounded-xl
                    px-6
                    py-4
                    transition-colors
                    duration-150
                    mt-4"
                    onClick={() => router.push("/foods-info")}
                >
                    食事情報
                </button>
            </div>
        </div>
    )
}