# gnu-radio-frontend

Process signals received by the SDR in order to obtain the processed signal data and graphics on them.

# Contribute

To execute and develop in local this project:

1. Check your Node version as [detailed here](#node-version).
2. Install dependencies inside the root folder with `npm install`.
3. Execute `npm run dev:react` to start react in the project.
4. Execute `npm run dev:electron` to start electron in the project.

## Available scripts

In the project directory, you can run:

### `npm run dev:react` and `npm run dev:electron`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

# Notes

## Node version

The current project is being developed with the Node version specified in the `.nvmrc` file. You can check your Node version with `node --version` and use/change it if appropiated or use something like [nvmrc](https://github.com/nvm-sh/nvm/blob/master/README.md) and execute `nvm use` in the root folder of the project to set to the project version.
