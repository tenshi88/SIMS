;(async () => {
    return
    const body = new URLSearchParams()
    body.append('action', 'get_categorized')
    const req = await fetch('http://localhost/api/student', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res.data)
})()

// 全校検索するか否かのチェックボックス
const allSchoolSearch = document.getElementById('allSchoolSearch')
// 卒業生を表示するか否かのチェックボックス
const graduated = document.getElementById('graduated')
// 検索ボタン
const studentSearchBtn = document.getElementById('studentSearchBtn')

//reloadPage(categorizedStudents)

// ページの再読み込み
function reloadPage(categorizedStudents) {
    const studentListNode = document.querySelector('#student-list')
    const buildStudentTr = (students) => {
        return students.reduce((tr, student) => {
            return `${tr}
            <tr onclick="location.href = '/${student.school}/student_detail/${student.id}'">
                <td>${student.name}</td>
                <td>${student.name_kana}</td>
                <td>${student.gender}</td>
                <td>${student.age}</td>
            </tr>
            `
        }, '')
    }
    let mainHtml = ''
    for (const list of categorizedStudents) {
        if (!list.students.length) continue
        if (!list.is_open && !graduated.checked) continue
        mainHtml += `
            <div class="row g-1 mt-3">
                <div class="col-auto">
                    <h5 class="pt-1">${list.school} ${list.class_number} ${list.class_name}</h5>
                    <span>${list.open_date} ～ ${list.close_date}</span>
                </div>
            </div>
            <div class="row g-1">
                <table id="student-table" class="table table-striped table-hover mb-0">
                    <thead>
                        <tr>
                            <th>名前</th>
                            <th>フリガナ</th>
                            <th>性別</th>
                            <th>年齢</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${buildStudentTr(list.students)}
                    </tbody>
                </table>
            </div>
        `
    }
    studentListNode.innerHTML = mainHtml
}

allSchoolSearch.addEventListener('change', async (event) => {
    if (event.target.checked) {
        if (allStudents === null) {
            const body = new URLSearchParams()
            body.append('action', 'get_categorized')
            const req = await fetch('http://localhost/api/student', { method: 'POST', body: body })
            const res = await req.json()
            allStudents = res.data
        }
    }
})

// 検索(検索対象は名前、クラス、年齢、ALL)
studentSearchBtn.addEventListener('click', async () => {
    const searchStr = document.getElementById('searchText').value
    const searchType = document.getElementById('searchType').value
    const isAllSchoolSearch = allSchoolSearch.checked
    const students = isAllSchoolSearch ? allStudents : categorizedStudents
    const result = students.map((list) => {
        return {
            ...list,
            students: list.students.filter((student) => {
                if (searchType === 'all') {
                    return Object.values(student).some((value) => {
                        return value.toString().includes(searchStr)
                    })
                } else {
                    return student[searchType].toString().includes(searchStr)
                }
            }),
        }
    })
    // 検索結果を表示
    reloadPage(result)
})
