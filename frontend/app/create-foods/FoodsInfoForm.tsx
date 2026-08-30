"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function FoodsInfoFormPage() {
    const [foodName, setFoodsName] = useState("");
    const [calories, setCalories] = useState("");
    const [protein, setProtein] = useState("");
    const router = useRouter();

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
        if (res.status === 401) {
            localStorage.removeItem("access_token");
            router.push("/login");
            return;
        }

        if (!res.ok) {
            console.error("登録失敗" + res.status);
            const text = await res.text();
            console.log("response", text);
            setMessage("登録に失敗しました。");
            return;
        }

        const data = await res.json();
        console.log("登録成功", data);
        setFoodsName("");
        setCalories("");
        setProtein("");
        setMessage("登録が完了しました。");
    };

    const [message, setMessage] = useState("");

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
                {message && (
                    <p className="mt-4 text-center">{message}</p>
                )}
            </form>
        </div>
    );
};