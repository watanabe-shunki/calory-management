"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import FoodsInfoFrom from "./FoodsInfoForm";

export default function FoodsInfoPage() {
    const [intakes, setIntakes] = useState<any[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [message, setMessage] = useState<string | null>(null);
    const router = useRouter();
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
                setMessage("食事情報が見つかりませんでした。登録してください。");
            }
            setIntakes(intakes);
        } finally {
            setIsLoading(false);
        }
    };
    useEffect(() => {
        fetchIntakes();
    }, []);
if (isLoading) {
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
            <h1 className="text-2xl font-bold mb-6">食事一覧</h1>
            <table className="table-auto w-full border-collapse border border-gray-300">
                <thead>
                    <tr>
                        <th className="border border-gray-300 px-4 py-2">食事名</th>
                        <th className="border border-gray-300 px-4 py-2">カロリー</th>
                        <th className="border border-gray-300 px-4 py-2">タンパク質</th>
                    </tr>
                </thead>
                <tbody>
                    {intakes.map((intake: any, index: number) => (
                        <tr key={index}>
                            <td className="border border-gray-300 px-4 py-2">{intake.food_name}</td>
                            <td className="border border-gray-300 px-4 py-2">{intake.calory} kcal</td>
                            <td className="border border-gray-300 px-4 py-2">{intake.protein} g</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            {message && (
                <p className="mt-4 text-green-500 font-bold">{message}</p>
            )}
            <p>合計カロリー: {all_calory} kcal</p>
            <p>合計タンパク質: {all_protein} g</p>

            <FoodsInfoFrom onSuccess={fetchIntakes}/>
        </div>
    );
}