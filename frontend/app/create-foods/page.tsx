"use client";

import { useState } from "react";

export default function FoodsInfoFormPage() {
    const [foodName, setFoodsName] = useState("");
    const [calories, setCalories] = useState("");
    const [protein, setProtein] = useState("");

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        const res = await fetch("http://localhost:8000/create_foods_info", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                foods_name: foodName,
                calory: Number(calories),
                protein: Number(protein),
            }),
        });

        if (!res.ok) {
            console.error("登録失敗" + res.status);
            const text = await res.text();
            console.log("response", text);
            return;
        }

        const data = await res.json();
        console.log("登録成功", data);
    };

    return (
        <div className="container-app">
            <h1 className="text-2xl font-bold mb-4">食品情報登録</h1>
            
            <form onSubmit={handleSubmit}>
                <div>
                    <label>食品名:</label>
                    <input
                        className="input"
                        type="text"
                        value={foodName}
                        onChange={(e) => setFoodsName(e.target.value)}
                />
                </div>
                <div>
                    <label>カロリー:</label>
                    <input
                        className="input"
                        type="number"
                        value={calories}
                        onChange={(e) => setCalories(e.target.value)}
                    />
                </div>
                <div>
                    <label>タンパク質:</label>
                    <input
                        className="input"
                        type="number"
                        value={protein}
                        onChange={(e) => setProtein(e.target.value)}
                    />
                </div>
                <button type="submit" className="btn btn-primary w-full">
                    登録
                </button>
            </form>
        </div>
    );
};