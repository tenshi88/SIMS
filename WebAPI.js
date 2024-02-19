//////////////////////////////////////////////////////////////////////////////////////////////////////
// 生徒情報の登録、削除、表示、編集を行うAPI
// 追加
;(async () => {
    const nameList = ['あああ', 'いいい', 'ううう', 'えええ', 'おおお']
    const nameKanaList = ['アアア', 'イイイ', 'ウウウ', 'エエエ', 'オオオ']
    const classList = ['Aコース', 'Bコース', 'Cコース', 'Dコース', 'Eコース', 'Fコース']
    let body
    for (let i = 0; i < nameList.length; i++) {
        for (const cls of classList) {
            body = new URLSearchParams()
            body.append('action', 'register')
            body.append('name', nameList[i])
            body.append('name_kana', nameKanaList[i])
            body.append('age', 20)
            body.append('class_name', cls)
            body.append('gender', 1)
            body.append('birthday', '2000-01-01')
            body.append('address', '大阪府大阪市中央区x-xx-xx')
            body.append('phone', '123-456-7890')
            body.append('email', 'aaa@gmail.com')
            body.append('gmail', 'bbb@gmail.com')
            body.append('school', '天満橋校')
            body.append('note', '備考')
            const req = await fetch('http://localhost/api/student', { method: 'POST', body: body })
            const res = await req.json()
            console.log(res)
        }
    }
})()

// 削除
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'delete')
    body.append('id', 1)
    const req = await fetch('http://localhost/api/student', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()

// 全削除
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'delete_all')
    const req = await fetch('http://localhost/api/student', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()

// 取得
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'get')
    body.append('school', '天満橋校')
    body.append('id', 1)
    const req = await fetch('http://localhost/api/student', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()

// 更新
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'update')
    body.append('id', 1)
    body.append('name', 'あいうえお')
    body.append('name_kana', 'アイウエオ')
    body.append('age', 20)
    body.append('class_name', 'ウェブプログラマー養成コース')
    body.append('gender', 1)
    body.append('birthday', '2000-01-01')
    body.append('address', '大阪府大阪市中央区x-xx-xx')
    body.append('phone', '123-456-7890')
    body.append('email', 'aaa@gmail.com')
    body.append('gmail', 'bbb@gmail.com')
    body.append('school', '天満橋校')
    body.append('note', '備考')

    const req = await fetch('http://localhost/api/student', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()
//////////////////////////////////////////////////////////////////////////////////////////////////////
// 学校の登録、削除、取得、更新を行うAPI
// 追加
;(async () => {
    const schools = ['本町校', '天満橋校', '心斎橋校', '三宮校']
    for (const school of schools) {
        const body = new URLSearchParams()
        body.append('action', 'register')
        body.append('name', school)
        const req = await fetch('http://localhost/api/school', { method: 'POST', body: body })
        const res = await req.json()
        console.log(res)
    }
})()

// 削除
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'delete')
    body.append('id', 1)
    const req = await fetch('http://localhost/api/school', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()

// 全取得
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'get')
    const req = await fetch('http://localhost/api/school', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()

// 更新
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'update')
    body.append('id', 1)
    body.append('name', '天満橋校')
    const req = await fetch('http://localhost/api/school', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()
//////////////////////////////////////////////////////////////////////////////////////////////////////
// クラスの登録、削除、取得、更新を行うAPI
// 追加
;(async () => {
    const classes = ['Aコース', 'Bコース', 'Cコース', 'Dコース', 'Eコース', 'Fコース']
    const openDates = ['2023-05-01', '2023-06-01', '2023-07-01', '2023-08-01', '2023-09-01', '2023-10-01']
    const closeDates = ['2023-11-30', '2023-12-31', '2024-01-31', '2024-02-29', '2024-03-31', '2024-04-30']
    for (let i = 0; i < classes.length; i++) {
        const body = new URLSearchParams()
        body.append('action', 'register')
        body.append('name', classes[i])
        body.append('class_number', 1001 + i)
        body.append('open_date', openDates[i])
        body.append('close_date', closeDates[i])
        const req = await fetch('http://localhost/api/class', { method: 'POST', body: body })
        const res = await req.json()
        console.log(res)
    }
})()

// 削除
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'delete')
    body.append('id', 1)
    const req = await fetch('http://localhost/api/class', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()

// 全取得
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'get')
    const req = await fetch('http://localhost/api/class', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()

// 更新
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'update')
    body.append('id', 1)
    body.append('name', 'ウェブプログラマー養成コース')
    body.append('class_number', 1001)
    body.append('open_date', '2023-01-01')
    body.append('close_date', '2023-12-31')
    const req = await fetch('http://localhost/api/class', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()
//////////////////////////////////////////////////////////////////////////////////////////////////////
// ユーザの登録、削除、取得、更新を行うAPI
// 追加
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'register')
    body.append('user_id', '0000')
    body.append('password', 'abcd')
    const req = await fetch('http://localhost/api/user', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()

// 削除
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'delete')
    body.append('id', 1)
    const req = await fetch('http://localhost/api/user', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()

// 全取得
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'get')
    const req = await fetch('http://localhost/api/user', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()

// 更新
;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'update')
    body.append('id', 1)
    body.append('user_id', '0000')
    body.append('password', 'abcd')
    const req = await fetch('http://localhost/api/user', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()
