"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function BodyInfoFormPage() {
    const access_token = localStorage.getItem("token");
    const [height, setHeight] = useState("");
    const [weight, setWeight] = useState("");
    const [activityStatus, setActivityStatus] = useState("OFFICE");
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        const res = await fetch(`http://localhost:8000/create_body_info`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${access_token}`,
            },
            body: JSON.stringify({
                height,
                weight,
                activity_status: activityStatus,
            }),
        });

        if (!res.ok) {
            console.error("登録失敗" + res.status);
            console.log("status", res.status);
            const text = await res.text();
            console.log("response", text);

            return;
        }

        const data = await res.json();
        router.refresh();
        console.log("登録成功", data);
        setHeight("");
        setWeight("");
        setActivityStatus("OFFICE");
        setMessage("身体情報が正常に登録されました。");

    };

    const [message, setMessage] = useState("");

    return (
        <div className="container-app">
            <h1 className="text-2xl font-bold mb-4">身体情報登録</h1>

            <form onSubmit={handleSubmit} className="card space-y-4">
                <div>
                    <label>身長</label>
                    <input
                        className="input"
                        value={height}
                        onChange={(e) => setHeight(e.target.value)}
                        placeholder="175"
                    />
                </div>

                <div>
                    <label>体重</label>
                    <input
                        className="input"
                        value={weight}
                        onChange={(e) => setWeight(e.target.value)}
                        placeholder="76"
                    />
                </div>

                <div>
                    <label>活動レベル</label>
                    <select
                        className="input"
                        value={activityStatus}
                        onChange={(e) => setActivityStatus(e.target.value)}
                    >
                        <option value="OFFICE">OFFICE</option>
                        <option value="LIGHT">LIGHT</option>
                        <option value="ACTIVE">ACTIVE</option>
                    </select>
                </div>

                <button type="submit" className="btn btn-primary w-full">
                    登録
                </button>
                {message && (
                    <p className="mt-4 text-center">{message}</p>
                )}
            </form>
        </div>
    );
}