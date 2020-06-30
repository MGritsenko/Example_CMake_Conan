include(public_headers)
include(GenerateExportHeader)

set(LEXER-CORE_TARGET_NAME core)
set(LEXER-CORE_NAMESPACE lexer-core)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)

find_package(Qt5 COMPONENTS
	Core
	REQUIRED
)

add_library(${LEXER-CORE_TARGET_NAME} lexer.h lexer.cpp)

set_target_properties(${LEXER-CORE_TARGET_NAME} PROPERTIES
	DEFINE_SYMBOL LEXER_CORE_EXPORTS
)

generate_export_header(${LEXER-CORE_TARGET_NAME}
	 BASE_NAME ${LEXER-CORE_NAMESPACE}
	 EXPORT_FILE_NAME "${CMAKE_CURRENT_BINARY_DIR}/include/${LEXER-CORE_NAMESPACE}/exports.h"
)

target_public_headers(${LEXER-CORE_TARGET_NAME} lexer.h)

target_include_directories(${LEXER-CORE_TARGET_NAME}
	PRIVATE
		"${CMAKE_CURRENT_BINARY_DIR}/include"
)

target_link_libraries(${LEXER-CORE_TARGET_NAME}
	PUBLIC
		Qt5::Core
)

build_public_headers(${LEXER-CORE_TARGET_NAME}
	HEADER_NAMESPACE ${LEXER-CORE_NAMESPACE}
	SRC_ROOT "${PROJECT_SOURCE_DIR}/src/core"
)

# define installing rules for target files and associate them with an export
install(TARGETS ${LEXER-CORE_TARGET_NAME}
	EXPORT ${LEXER_EXPORT_NAME}
)

install_public_headers(${LEXER-CORE_TARGET_NAME})