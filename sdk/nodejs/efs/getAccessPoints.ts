// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides information about multiple Elastic File System (EFS) Access Points.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const test = pulumi.output(aws.efs.getAccessPoints({
 *     fileSystemId: "fs-12345678",
 * }, { async: true }));
 * ```
 */
export function getAccessPoints(args: GetAccessPointsArgs, opts?: pulumi.InvokeOptions): Promise<GetAccessPointsResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("aws:efs/getAccessPoints:getAccessPoints", {
        "fileSystemId": args.fileSystemId,
    }, opts);
}

/**
 * A collection of arguments for invoking getAccessPoints.
 */
export interface GetAccessPointsArgs {
    /**
     * EFS File System identifier.
     */
    readonly fileSystemId: string;
}

/**
 * A collection of values returned by getAccessPoints.
 */
export interface GetAccessPointsResult {
    /**
     * Set of Amazon Resource Names (ARNs).
     */
    readonly arns: string[];
    readonly fileSystemId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Set of identifiers.
     */
    readonly ids: string[];
}
