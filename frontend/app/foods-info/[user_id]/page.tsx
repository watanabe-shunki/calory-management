export default async function FoodsInfoPage() {
    const user_id = 1;

    const res = await fetch(
        `http://localhost:8000/get_intakes_info/${user_id}`,
        { cache: "no-store"}
    );

    const intakes = await res.json()
    
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
            <p>合計カロリー: {all_calory} kcal</p>
            <p>合計タンパク質: {all_protein} g</p>
        </div>
    );
}