// モーダルの表示/非表示
class Modal {
    static element = document.getElementById('modal-main')
    static label = this.element.querySelector('#modal-label-main')
    static footer = this.element.querySelector('.modal-footer')
    static body = this.element.querySelector('.modal-body')
    static modal = null
    static show(label, body, footer) {
        this.label.textContent = label
        this.body.innerHTML = body
        this.footer.innerHTML = footer
        this.modal = new bootstrap.Modal(this.element)
        this.modal.show()
    }
    static hide() {
        this.modal.hide()
    }
}

// サブモーダルの表示/非表示
class SubModal extends Modal {
    static element = document.getElementById('modal-sub')
    static label = this.element.querySelector('#modal-label-sub')
    static footer = this.element.querySelector('.modal-footer')
    static body = this.element.querySelector('.modal-body')
}

// ユーザー編集/追加/削除モーダルの表示
function editUser(id, user_id, password) {
    const label = 'ユーザーを' + (id ? '編集' : '追加')
    let footer = ''
    // ユーザーを編集する場合、更新ボタンと削除ボタンを表示する
    if (label === 'ユーザーを編集') {
        footer = `
            <button type="button" id="delete-confirm" class="btn btn-danger">削除</button>
            <button type="button" name="submit-api" id="update" class="btn btn-primary">更新</button>
        `
    // ユーザーを追加する場合、追加ボタンのみを表示する
    } else {
        footer = `
            <button type="button" name="submit-api" id="register" class="btn btn-primary">追加</button>
        `
    }
    // モーダルのbody
    const body = `
        <form autocomplete="off">
            <div>
                <label for="user_id">ユーザーID<span class="text-danger">*</span></label>
                <input class="form-control my-2" type="text" id="user_id" name="user_id" placeholder="ユーザーID" pattern="^[a-zA-Z0-9]+$" minlength="4" maxlength="64" value="${
                    user_id ?? ''
                }" required>
                <div class="invalid-feedback" data-empty="ユーザーIDを入力してください" data-invalid="4～64文字の半角英数字で入力してください"></div>
            </div>
            <div>
                <label for="password">パスワード<span class="text-danger">*</span></label>
                <input class="form-control my-2" type="password" id="password" name="password" placeholder="パスワード" pattern="^[a-zA-Z0-9]+$" minlength="4" maxlength="64" value="${
                    password ?? ''
                }" required>
                <div class="invalid-feedback" data-empty="パスワードを入力してください" data-invalid="4～64文字の半角英数字で入力してください"></div>
            </div>
        </form>
    `
    // モーダルを表示
    Modal.show(label, body, footer)

    // 更新/追加ボタンが押されたときの確認処理
    document.querySelector('[name=submit-api]').addEventListener('click', async (event) => {
        const path = 'user'
        const action = event.target.id
        updateConfirm(event, id, label, path, action)
    })

    // 削除ボタンが押されたときの確認処理
    Modal.footer.querySelector('#delete-confirm')?.addEventListener('click', (_) => {
        const label = 'ユーザーを削除'
        const path = 'user'
        deleteConfirm(id, label, path)
    })

    // 入力時のバリデーションチェック
    document.getElementById('user_id').addEventListener('input', validation)
    document.getElementById('password').addEventListener('input', validation)
}

// 学校編集/追加/削除モーダルの表示
function editSchool(id, name) {
    const label = '学校を' + (id ? '編集' : '追加')
    let footer = ''
    // 学校を編集する場合、更新ボタンと削除ボタンを表示する 
    if (label === '学校を編集') {
        footer = `
            <button type="button" id="delete-confirm" class="btn btn-danger">削除</button>
            <button type="button" name="submit-api" id="update" class="btn btn-primary">更新</button>
        `
    // 学校を追加する場合、追加ボタンのみを表示する
    } else {
        footer = `
            <button type="button" name="submit-api" id="register" class="btn btn-primary">追加</button>
        `
    }
    // モーダルのbody
    const body = `
        <form autocomplete="off">
            <div>
                <label for="name">学校名<span class="text-danger">*</span></label>
                <input class="form-control my-2" type="text" id="name" name="name" placeholder="学校名" maxlength="64" value="${name ?? ''}" required>
                <div class="invalid-feedback" data-empty="学校名を入力してください" data-invalid="64文字以内で入力してください"></div>
            </div>
        </form>
    `
    // モーダルを表示
    Modal.show(label, body, footer)

    // 更新/追加ボタンが押されたときの確認処理
    document.querySelector('[name=submit-api]').addEventListener('click', async (event) => {
        const path = 'school'
        const action = event.target.id
        updateConfirm(event, id, label, path, action)
    })

    // 削除ボタンが押されたときの確認処理
    Modal.footer.querySelector('#delete-confirm')?.addEventListener('click', (_) => {
        const label = '学校を削除'
        const path = 'school'
        deleteConfirm(id, label, path)
    })

    // 入力時のバリデーションチェック
    document.getElementById('name').addEventListener('input', validation)
}

// クラス編集/追加/削除モーダルの表示
function editClass(id, name) {
    const label = 'クラスを' + (id ? '編集' : '追加')
    let footer = ''
    // クラスを編集する場合、更新ボタンと削除ボタンを表示する
    if (label === 'クラスを編集') {
        footer = `
            <button type="button" id="delete-confirm" class="btn btn-danger">削除</button>
            <button type="button" name="submit-api" id="update" class="btn btn-primary">更新</button>
        `
    // クラスを追加する場合、追加ボタンのみを表示する   
    } else {
        footer = `
            <button type="button" name="submit-api" id="register" class="btn btn-primary">追加</button>
        `
    }
    // モーダルのbody
    const body = `
        <form autocomplete="off">
            <div>
                <label for="name">クラス名<span class="text-danger">*</span></label>
                <input class="form-control my-2" type="text" id="name" name="name" placeholder="クラス名" maxlength="64" value="${name ?? ''}" required>
                <div class="invalid-feedback" data-empty="クラス名を入力してください" data-invalid="64文字以内で入力してください"></div>
            </div>
        </form>
    `
    // モーダルを表示
    Modal.show(label, body, footer)

    // 更新/追加ボタンが押されたときの確認処理
    document.querySelector('[name=submit-api]').addEventListener('click', async (event) => {
        const path = 'class'
        const action = event.target.id
        updateConfirm(event, id, label, path, action)
    })

    // 削除ボタンが押されたときの確認処理
    Modal.footer.querySelector('#delete-confirm')?.addEventListener('click', (_) => {
        const label = 'クラスを削除'
        const path = 'class'
        deleteConfirm(id, label, path)
    })

    // 入力時のバリデーションチェック
    document.getElementById('name').addEventListener('input', validation)
}

// ページの再読み込み
function reloadPage() {
    // テーブルのtbody要素を取得
    const userTableBody = document.querySelector('#user-table tbody')
    const schoolTableBody = document.querySelector('#school-table tbody')
    const classTableBody = document.querySelector('#class-table tbody')

    // テーブルの中身を再描画
    userTableBody.innerHTML = users.reduce((html, user) => {
        return `${html}
            <tr>
                <td>${user.id}</td>
                <td>${user.user_id}</td>
                <td>
                    <button type="button" name="edit-user" class="btn btn-primary" data-id="${user.id}" data-user-id="${user.user_id}" data-password="${user.password}" onclick="editUser(${user.id}, '${user.user_id}', '${user.password}')">編集</button>
                </td>
            </tr>
        `
    }, '')

    schoolTableBody.innerHTML = schools.reduce((html, school) => {
        return `${html}
            <tr>
                <td>${school.id}</td>
                <td>${school.name}</td>
                <td>
                    <button type="button" name="edit-school" class="btn btn-primary" data-id="${school.id}" data-school-name="${school.name}" onclick="editSchool(${school.id}, '${school.name}')">編集</button>
                </td>
            </tr>
        `
    }, '')

    classTableBody.innerHTML = classes.reduce((html, cls) => {
        return `${html}
            <tr>
                <td>${cls.id}</td>
                <td>${cls.name}</td>
                <td>
                    <button type="button" name="edit-class" class="btn btn-primary" data-id="${cls.id}" data-class-name="${cls.name}" onclick="editClass(${cls.id}, '${cls.name}')">編集</button>
                </td>
            </tr>
        `
    }, '')
}

// バリデーションチェック
function validation(event) {
    // 入力された要素
    const element = event.target
    // 入力された要素の次の要素(.invalid-feedback)
    const feedback = element.nextElementSibling
    // 入力が不正な場合、エラーメッセージを表示する
    if (!element.checkValidity()) {
        element.classList.add('is-invalid')
        element.classList.remove('is-valid')
        const errorMsg = feedback.getAttribute(element.value === '' ? 'data-empty' : 'data-invalid')
        feedback.textContent = errorMsg
        return
    }
    // 入力されている場合、エラーメッセージを非表示にする
    element.classList.add('is-valid')
    element.classList.remove('is-invalid')
    feedback.textContent = ''
}

// 共通のアクションハンドラ
async function handleAction(id, label, path, action, successMessage, event = null) {
    const body = `<p>本当に${label}しますか？</p>`
    const footer = `
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">キャンセル</button>
        <button type="button" name="submit-api" id="exec" class="btn btn-danger">${label}</button>
    `
    // サブモーダルを表示
    SubModal.show(label, body, footer)
    // 更新/追加/削除ボタンが押されたときの処理
    document.querySelector('#exec').addEventListener('click', async (_) => {
        // モーダルを非表示
        Modal.hide()
        try {
            // リクエストを送信し、エラーがなければ成功メッセージを表示する
            await fetchPostAndHandleError(event, path, action, id)
            SubModal.body.innerHTML = successMessage
            SubModal.footer.innerHTML = '<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">閉じる</button>'
            // データを更新し、ページを再読み込みする
            await updateData(path)
            reloadPage()
            // 2秒後にサブモーダルを非表示にする
            setTimeout(() => SubModal.hide(), 2000)
        } catch (error) {
            SubModal.label.textContent = 'エラーが発生しました'
            SubModal.body.innerHTML = `<p>${error}</p>`
        }
    })
}

// 更新/追加ボタンが押されたときの処理
function updateConfirm(event, id, label, path, action) {
    // モーダルの中のフォーム要素
    const modalContent = event.target.closest('.modal-content')
    const form = modalContent.querySelector('form')
    // バリデーションチェック
    const isValid = form.checkValidity()
    if (!isValid) {
        // バリデーションエラーがある場合、イベントをキャンセルする
        event.preventDefault()
        return
    }
    // バリデーションエラーがない場合、アクションハンドラを呼び出す
    handleAction(id, label, path, action, '操作を完了しました', event)
}

// 削除ボタンが押されたときの確認処理
function deleteConfirm(id, label, path) {
    // 削除ボタンが押されたときのアクションハンドラを呼び出す
    handleAction(id, label, path, 'delete', '削除完了しました')
}

// データの更新
async function updateData(path) {
    // ユーザー/学校/クラスのデータを取得
    let json = await fetchPostAndHandleError(null, path, 'get')
    // データを更新
    if (path === 'user') {
        users = json.data
    } else if (path === 'school') {
        schools = json.data
    } else if (path === 'class') {
        classes = json.data
    }
}

// fetchでPOSTリクエストを送信し、エラーがあった場合はエラーメッセージを表示する
async function fetchPostAndHandleError(event, path, action, id) {
    // サーバーからのレスポンスを取得
    let json = await fetchPost(event, path, action, id)
    // エラーメッセージがなければレスポンスを返す
    if (json.error === '') {
        return json
    // エラーメッセージがあればそれを投げる
    } else {
        throw new Error(json.error)
    }
}

// fetchでPOSTリクエストを送信
async function fetchPost(event, path, action, id) {
    // リクエストのbodyを作成
    const body = new URLSearchParams()
    // フォームの中身をbodyに追加
    if (event) {
        const form = event.target.closest('.modal-content').querySelector('form')
        for (const input of form.querySelectorAll('input')) {
            body.append(input.name, input.value)
        }
    }
    body.append('action', action)
    body.append('id', id)
    // リクエストを送信
    const url = `http://localhost/api/${path}`
    const req = await fetch(url, { method: 'POST', body: body })
    // サーバーからのレスポンスをjson形式で返す
    return req.json()
}