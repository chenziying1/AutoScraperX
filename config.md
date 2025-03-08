## 1. 基本配置

### `<span>urls</span>` （列表）

* **作用**：指定多个目标 URL。
* **示例**：
  ```
  options = {
      "urls": ["https://example.com/page1", "https://example.com/page2"]
  }
  ```

### `<span>url</span>` （字符串）

* **作用**：指定单个目标 URL。
* **示例**：
  ```
  options = {
      "url": "https://example.com"
  }
  ```

### `<span>headless</span>` （布尔值，默认 `<span>False</span>`）

* **作用**：是否启用无头模式。
* **示例**：
  ```
  options = {
      "headless": True
  }
  ```

### `<span>maximized</span>` （布尔值，默认 `<span>True</span>`）

* **作用**：是否启动时最大化窗口。
* **示例**：
  ```
  options = {
      "maximized": False
  }
  ```

---

## 2. 用户数据配置

### `<span>user_data_dir</span>` （字符串，路径）

* **作用**：指定 Chrome 用户数据目录。
* **示例**：
  ```
  options = {
      "user_data_dir": "C:/Users/Admin/AppData/Local/Google/Chrome/User Data"
  }
  ```

### `<span>profile_directory</span>` （字符串，默认 `<span>"Default"</span>`）

* **作用**：指定 Chrome 配置文件。
* **示例**：
  ```
  options = {
      "profile_directory": "Profile 1"
  }
  ```

---

## 3. 浏览器配置

### `<span>binary_location</span>` （字符串）

* **作用**：指定 Chrome 可执行文件路径。

### `<span>driver_executable_path</span>` （字符串）

* **作用**：指定 ChromeDriver 的路径。

### `<span>fastest</span>` （布尔值，默认 `<span>False</span>`）

* **作用**：启用后禁用一些功能以加速浏览器。

### `<span>mobile</span>` （布尔值，默认 `<span>False</span>`）

* **作用**：模拟移动端浏览器。

---

## 4. 日志配置

### `<span>logging_level</span>` （字符串，默认 `<span>None</span>`）

* **可选值**：`<span>"0"</span>` ~ `<span>"4"</span>`

---

## 5. 页面加载与超时

### `<span>page_load_timeout</span>` （整数，默认 `<span>1800</span>` 秒）

### `<span>enable_page_load_timeout</span>` （布尔值，默认 `<span>True</span>`）

### `<span>waiter_seconds</span>` （整数，默认 `<span>300</span>`）

---

## 6. Cookies 相关

### `<span>save_cookie(path: str = 'data/cookies.pkl')</span>`

* **作用**：存储 cookies。

### `<span>load_cookie(path: str = 'data/cookies.pkl', domain='')</span>`

* **作用**：加载 cookies。

---

## 7. 页面操作

* `<span>open(url: str = None)</span>`
* `<span>get_source()</span>`
* `<span>save_screenshot(file_path)</span>`
* `<span>wait_element(selector, by=By.XPATH, seconds=None)</span>`
* `<span>scroll_to_top()</span>`
* `<span>refresh()</span>`
* `<span>switch_tab(index=0)</span>`
* `<span>close_tab()</span>`
* `<span>quit()</span>`

---

## 8. 元素交互

* `<span>element(selector, by=By.CSS_SELECTOR)</span>`
* `<span>elements(selector, by=By.CSS_SELECTOR)</span>`
* `<span>comment(text, css_selector='#comment', reset=False, br=True)</span>`
* `<span>wait_for_element_and_execute(selector, by=By.CSS_SELECTOR, seconds=30)</span>`

---

## 9. 其他工具

### `<span>rm_space(text: str) -> str</span>`

* **作用**：去除字符串空格。

### `<span>random_id()</span>`

* **作用**：生成随机 ID。
