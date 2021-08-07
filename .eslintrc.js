module.exports = {
    extends: [
      'eslint:recommended',
      'plugin:react/recommended',
      'plugin:@typescript-eslint/recommended',
      'plugin:jest/recommended',
      'plugin:prettier/recommended'
    ],
    plugins: ['react', '@typescript-eslint', 'jest', 'prettier'],
    env: {
      browser: true,
      es6: true,
      jest: true,
    },
    globals: {
      Atomics: 'readonly',
      SharedArrayBuffer: 'readonly',
    },
    parser: '@typescript-eslint/parser',
    parserOptions: {
      ecmaFeatures: {
        jsx: true,
      },
      ecmaVersion: 2020,
      sourceType: 'module',
      project: './tsconfig.json',
    },
    rules: {
      'linebreak-style': 'off',
      'no-var': 'error',
      'brace-style': 'error',
      'prefer-template': 'error',
      'radix': 'error',
      'space-before-blocks': 'error',
      'import/prefer-default-export': 'off',
      'prettier/prettier': [
        'error',
        {
          singleQuote: true,
          endOfLine: 'auto'
        },
      ],
    },
    settings: {
      react: {
        pragma: 'React',
        version: 'detect'
      }
    },
    overrides: [
      {
        files: [
          '**/*.test.js',
          '**/*.test.jsx',
          '**/*.test.tsx',
          '**/*.spec.js',
          '**/*.spec.jsx',
          '**/*.spec.tsx',
        ],
        rules: {
          '@typescript-eslint/camelcase': 'off',
          'no-undef': 'off',
          '@typescript-eslint/no-explicit-any': 'off'
        },
        env: {
          jest: true,
        },
      },
    ],
  };