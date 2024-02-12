const modalMain = document.getElementById('modal-main')
const modalFooter = document.querySelector('.modal-footer')
const modalBody = document.querySelector('.modal-body')

// ユーザー編集/追加モーダルの表示
const editUserBtn = document.querySelectorAll('[name=edit-user]')
const addUserBtn = document.querySelector('[name=add-user]')
for (const el of [...editUserBtn, addUserBtn]) {
    el.addEventListener('click', editUser)
}

function editUser() {
    const title = this.name === 'edit-user' ? 'ユーザー編集' : 'ユーザー追加'
    const modal = new bootstrap.Modal(modalMain)
    const modalLabel = document.getElementById('modalLabel')
    modalLabel.textContent = title
    modalBody.innerHTML = `
        <form autocomplete="off">
            <div>
                <label for="user_id">ユーザーID<span class="text-danger">*</span></label>
                <input class="form-control my-2" type="text" id="user_id" name="user_id" placeholder="ユーザーID" pattern="^[a-zA-Z0-9]+$" maxlength="64" required>
                <div class="invalid-feedback" data-empty="ユーザーIDを入力してください" data-invalid="64文字以内の半角英数字で入力してください"></div>
            </div>
            <div>
                <label for="password">パスワード<span class="text-danger">*</span></label>
                <input class="form-control my-2" type="password" id="password" name="password" placeholder="パスワード" maxlength="64" required>
                <div class="invalid-feedback" data-empty="パスワードを入力してください" data-invalid="64文字以内の半角英数字で入力してください"></div>
            </div>
        </form>
    `
    if (title === 'ユーザー編集') {
        document.getElementById('user_id').value = this.getAttribute('data-user-id')
        document.getElementById('password').value = this.getAttribute('data-password')
        modalFooter.innerHTML = `
            <button type="button" id="delete" class="btn btn-danger">削除</button>
            <button type="button" name="submit-api" id="update" class="btn btn-primary">更新</button>
        `
    } else {
        modalFooter.innerHTML = `
            <button type="button" name="submit-api" id="add" class="btn btn-primary">追加</button>
        `
    }
    modal.show()

    const userIdInput = document.getElementById('user_id')
    const passwordInput = document.getElementById('password')

    // 更新/追加ボタンが押されたときの動作
    document.querySelector('[name=submit-api]').addEventListener('click', async (event) => {
        let isVarid = validate(userIdInput)
        isVarid = validate(passwordInput) && isVarid
        console.log(isVarid)
        // バリデーションチェックでエラーがあった場合、イベントを取り消す
        if (!isVarid) {
            event.preventDefault()
            return
        }
        // fetchでPOSTリクエストを送信
        const action = event.target.id === 'add' ? 'register' : 'update'
        console.log(this.getAttribute('data-id'))
        await fetchPost(event, 'http://localhost/api/user', action, this.getAttribute('data-id'))
    })

    // 削除ボタンが押されたときの動作
    document.querySelector('.modal-footer > button').addEventListener('click', async (event) => {
        await fetchPost(event, 'http://localhost/api/user', 'delete', this.getAttribute('data-id'))
    })

    // 入力時のバリデーションチェック
    userIdInput.addEventListener('input', validate.bind(null, userIdInput))
    passwordInput.addEventListener('input', validate.bind(null, passwordInput))
}

// 学校編集/追加モーダルの表示
const editSchoolBtn = document.querySelectorAll('[name=edit-school]')
const addSchoolBtn = document.querySelector('[name=add-school]')
for (const el of [...editSchoolBtn, addSchoolBtn]) {
    el.addEventListener('click', editSchool)
}

function editSchool() {
    const title = this.name === 'edit-school' ? '学校編集' : '学校追加'
    const modal = new bootstrap.Modal(modalMain)
    const modalLabel = document.getElementById('modalLabel')
    modalLabel.textContent = title
    modalBody.innerHTML = `
        <form autocomplete="off">
            <div>
                <label for="name">学校名<span class="text-danger">*</span></label>
                <input class="form-control my-2" type="text" id="name" name="name" placeholder="学校名" maxlength="64" required>
                <div class="invalid-feedback" data-empty="学校名を入力してください" data-invalid="64文字以内で入力してください"></div>
            </div>
        </form>
    `
    if (title === '学校編集') {
        document.getElementById('name').value = this.getAttribute('data-school-name')
        modalFooter.innerHTML = `
            <button type="button" id="delete" class="btn btn-danger">削除</button>
            <button type="button" name="submit-api" id="update" class="btn btn-primary">更新</button>
        `
    } else {
        modalFooter.innerHTML = `
            <button type="button" name="submit-api" id="add" class="btn btn-primary">追加</button>
        `
    }
    modal.show()

    const nameInput = document.getElementById('name')

    // 更新/追加ボタンが押されたときの動作
    document.querySelector('[name=submit-api]').addEventListener('click', async (event) => {
        const isVarid = validate(nameInput)
        // バリデーションチェックでエラーがあった場合、イベントを取り消す
        if (!isVarid) {
            event.preventDefault()
            return
        }
        // fetchでPOSTリクエストを送信
        const action = event.target.id === 'add' ? 'register' : 'update'
        await fetchPost(event, 'http://localhost/api/school', action, this.getAttribute('data-id'))
    })

    // 削除ボタンが押されたときの動作
    document.querySelector('.modal-footer > button').addEventListener('click', async (event) => {
        await fetchPost(event, 'http://localhost/api/school', 'delete', this.getAttribute('data-id'))
    })

    // 入力時のバリデーションチェック
    nameInput.addEventListener('input', validate.bind(null, nameInput))
}

// クラス編集/追加モーダルの表示
const editClassBtn = document.querySelectorAll('[name=edit-class]')
const addClassBtn = document.querySelector('[name=add-class]')
for (const el of [...editClassBtn, addClassBtn]) {
    el.addEventListener('click', editClass)
}

function editClass() {
    const title = this.name === 'edit-class' ? 'クラス編集' : 'クラス追加'
    const modal = new bootstrap.Modal(modalMain)
    const modalLabel = document.getElementById('modalLabel')
    modalLabel.textContent = title
    modalBody.innerHTML = `
        <form autocomplete="off">
            <div>
                <label for="name">クラス名<span class="text-danger">*</span></label>
                <input class="form-control my-2" type="text" id="name" name="name" placeholder="クラス名" maxlength="64" required>
                <div class="invalid-feedback" data-empty="クラス名を入力してください" data-invalid="64文字以内で入力してください"></div>
            </div>
        </form>
    `
    if (title === 'クラス編集') {
        document.getElementById('name').value = this.getAttribute('data-class-name')
        modalFooter.innerHTML = `
            <button type="button" id="delete" class="btn btn-danger">削除</button>
            <button type="button" name="submit-api" id="update" class="btn btn-primary">更新</button>
        `
    } else {
        modalFooter.innerHTML = `
            <button type="button" name="submit-api" id="add" class="btn btn-primary">追加</button>
        `
    }
    modal.show()

    const nameInput = document.getElementById('name')

    // 更新/追加ボタンが押されたときの動作
    document.querySelector('[name=submit-api]').addEventListener('click', async (event) => {
        const isVarid = validate(nameInput)
        // バリデーションチェックでエラーがあった場合、イベントを取り消す
        if (!isVarid) {
            event.preventDefault()
            return
        }
        // fetchでPOSTリクエストを送信
        const action = event.target.id === 'add' ? 'register' : 'update'
        await fetchPost(event, 'http://localhost/api/class', action, this.getAttribute('data-id'))
    })

    // 削除ボタンが押されたときの動作
    document.querySelector('.modal-footer > button').addEventListener('click', async (event) => {
        await fetchPost(event, 'http://localhost/api/class', 'delete', this.getAttribute('data-id'))
    })

    // 入力時のバリデーションチェック
    nameInput.addEventListener('input', validate.bind(null, nameInput))
}

// バリデーションチェック
function validate(element) {
    const feedback = element.nextElementSibling
    // 入力が不正な場合、エラーメッセージを表示する
    if (!element.checkValidity()) {
        element.classList.add('is-invalid')
        element.classList.remove('is-valid')
        const errorMsg = feedback.getAttribute(element.value === '' ? 'data-empty' : 'data-invalid')
        feedback.textContent = errorMsg
        return false
    }
    // 入力されている場合、エラーメッセージを非表示にする
    element.classList.add('is-valid')
    element.classList.remove('is-invalid')
    feedback.textContent = ''
    return true
}

// fetchでPOSTリクエストを送信
async function fetchPost(event, url, action, id) {
    const form = event.target.closest('.modal-content').querySelector('form')
    const body = new URLSearchParams()
    for (const input of form.querySelectorAll('input')) {
        body.append(input.name, input.value)
    }
    body.append('action', action)
    body.append('id', id)
    const req = await fetch(url, { method: 'POST', body: body })
    const res = await req.json()
    console.log(res)
}
