;(async () => {
    const body = new URLSearchParams()
    body.append('action', 'get_divide_by_class')
    //body.append('school', '天満橋校')
    const req = await fetch('http://localhost/api/student', { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
})()

let school = 'aaa'

// ページの再読み込み
function reloadPage() {
    const studentListNode = document.querySelector('#student-list')
    studentListNode.innerHTML = ''
    for (const list of studentsByClass) {
        if (!list.length) continue
        const tr = ``
        const mainHtml = `
    <div class="row g-1 mt-3">
        <div class="col-auto">
            <h5 class="pt-1">${school} ${list.class_name}</h5>
        </div>
    </div>
    <div class="row g-1">
        <table id="student-table" class="table table-striped table-hover mb-0">
            <thead>
                <tr>
                    <th>名前</th>
                    <th>性別</th>
                    <th>年齢</th>
                </tr>
            </thead>
            <tbody>
            {% for student in list.students %}
            <tr>
                <td>{{ student.name }}</td>
                <td>{{ student.gender }}</td>
                <td>{{ student.age }}</td>
                <td>
                    <button class="btn btn-primary" name="edit-student" onclick="location.href='/{{ school.name }}/student_detail/{{ student.id }}'">詳細</button>
                </td>
            </tr>
            {% endfor %}
            </tbody>
        </table>
    </div>`
    }
    
}