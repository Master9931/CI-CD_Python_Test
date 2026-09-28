# 将项目推送到GitHub的步骤指南

## 步骤1：在GitHub上创建新仓库

1. 登录到 [GitHub.com](https://github.com)
2. 点击右上角的 "+" 图标，选择 "New repository"
3. 填写仓库名称（例如：`ci-cd`）
4. 选择仓库可见性（公开或私有）
5. 可选：添加描述
6. **不要** 初始化带有README、.gitignore或许可证（我们已经有了本地文件）
7. 点击 "Create repository"

## 步骤2：将本地仓库关联到GitHub远程仓库

创建仓库后，GitHub会显示类似这样的URL：
- HTTPS：`https://github.com/your-username/ci-cd.git`
- SSH：`git@github.com:your-username/ci-cd.git`

在您的本地项目目录中，运行以下命令（将URL替换为您的实际仓库URL）：

```bash
# 添加远程仓库（使用HTTPS）
git remote add origin https://github.com/your-username/ci-cd.git

# 或者使用SSH（如果您已设置SSH密钥）
# git remote add origin git@github.com:your-username/ci-cd.git
```

## 步骤3：将代码推送到GitHub

```bash
# 将主分支推送到GitHub
git push -u origin master

# 如果您的默认分支是main而不是master，使用：
# git push -u origin main
```

## 步骤4：验证推送成功

推送完成后，刷新您的GitHub仓库页面，您应该能看到：
- 所有项目文件已上传
- 提交历史可见
- CI/CD工作流程文件 (.github/workflows/ci.yml) 已包含

## 常见问题排查

### 权限错误
如果遇到权限错误，请确保：
- 使用HTTPS时，您的GitHub用户名和密码（或个人访问令牌）正确
- 使用SSH时，您的SSH密钥已正确添加到GitHub账户

### 分支名称问题
如果推送时看到关于分支名称的警告，您可以：
```bash
# 将本地master分支推送到远程main分支（如果需要）
git push -u origin master:main
```

### 大文件问题
如果遇到大文件错误，请检查.gitignore文件是否正确排除了不必要的文件。

## 后续步骤

一旦代码成功推送到GitHub：
1. 您的GitHub Actions CI/CD工作流程（.github/workflows/ci.yml）将自动触发
2. 您可以在GitHub仓库的 "Actions" 选项卡中查看构建状态
3. 后续的更改可以使用常规的git流程：
   ```bash
   git add .
   git commit -m "您的提交信息"
   git push
   ```